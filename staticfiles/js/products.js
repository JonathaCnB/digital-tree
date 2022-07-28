document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
})

document.addEventListener('htmx:afterRequest', (e) => {
    if (e.target.id === 'form-cad-group') {
        $('#modal-cad-group').modal('hide');
    }
    if (e.target.id === 'form-cad-sub-group') {
        $('#modal-cad-sub-group').modal('hide');
    }
    if (e.target.id === 'form-product-cad') {
        $('#modal-cad-product').modal('hide');
    }
    if (e.target.id === 'form-product-update') {
        $('#modal-cad-product').modal('hide');
    }
    if (e.target.id === 'form-exclude-product') {
        $('#modal-cad-group').modal('hide');
    }
})

; (function () {

    htmx.on('showMessage', (e) => {
        const value = e.detail.value
        $(document).Toasts('create', {
            title: 'Acão Realizada',
            autohide: true,
            position: 'bottomLeft',
            delay: 3000,
            body: value
        })
    })
})()


