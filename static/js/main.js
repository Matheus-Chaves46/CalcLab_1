// Função para formatar números com casas decimais
function formatarNumero(numero, casasDecimais = 2) {
    return Number(numero).toFixed(casasDecimais);
}

// Função para validar campos numéricos
function validarNumero(valor) {
    return !isNaN(valor) && valor !== '';
}

// Função para mostrar mensagem de erro
function mostrarErro(mensagem) {
    $('#resultado-container').html(`
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `);
}

// Função para mostrar mensagem de sucesso
function mostrarSucesso(mensagem) {
    $('#resultado-container').html(`
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `);
}

// Função para copiar resultado para a área de transferência
function copiarResultado(texto) {
    navigator.clipboard.writeText(texto).then(() => {
        mostrarSucesso('Resultado copiado para a área de transferência!');
    }).catch(() => {
        mostrarErro('Não foi possível copiar o resultado.');
    });
}

// Função para limpar formulário
function limparFormulario() {
    $('#calculo-form')[0].reset();
    $('#resultado-container').empty();
}

// Função para verificar se todos os campos obrigatórios estão preenchidos
function validarFormulario(form) {
    let valido = true;
    form.find('[required]').each(function() {
        if (!$(this).val()) {
            $(this).addClass('is-invalid');
            valido = false;
        } else {
            $(this).removeClass('is-invalid');
        }
    });
    return valido;
}

// Inicialização quando o documento estiver pronto
$(document).ready(function() {
    // Adiciona validação de formulário Bootstrap
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Adiciona botão de copiar resultado
    $(document).on('click', '.btn-copy', function() {
        const resultado = $(this).data('resultado');
        copiarResultado(resultado);
    });

    // Adiciona botão de limpar formulário
    $(document).on('click', '.btn-clear', function() {
        limparFormulario();
    });

    // Adiciona máscara para campos numéricos
    $(document).on('input', 'input[type="number"]', function() {
        this.value = this.value.replace(/[^0-9.-]/g, '');
    });

    // Adiciona tooltip para botões
    $('[data-bs-toggle="tooltip"]').tooltip();

    // Adiciona comportamento para campos dependentes
    $(document).on('change', 'select[data-depends-on]', function() {
        const dependsOn = $(this).data('depends-on');
        const dependentValue = $(`#${dependsOn}`).val();
        
        if (dependentValue) {
            $(this).prop('disabled', false);
        } else {
            $(this).prop('disabled', true);
            $(this).val('');
        }
    });
}); 