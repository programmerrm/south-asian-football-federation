document.addEventListener('DOMContentLoaded', function () {

    function toggleFields(row) {
        const typeField = row.querySelector('select[id$="-type"]');
        if (!typeField) return;

        const textField = row.querySelector('.field-text');
        const imageField = row.querySelector('.field-image');
        const adsField = row.querySelector('.field-ads');

        function updateVisibility() {
            const value = typeField.value;

            if (textField) textField.style.display = (value === 'text') ? '' : 'none';
            if (imageField) imageField.style.display = (value === 'image') ? '' : 'none';
            if (adsField) adsField.style.display = (value === 'ad') ? '' : 'none';
        }

        typeField.addEventListener('change', updateVisibility);
        updateVisibility();
    }

    function init() {
        const rows = document.querySelectorAll('.dynamic-newsdescription_set');
        rows.forEach(toggleFields);
    }

    document.addEventListener('formset:added', function(event) {
        toggleFields(event.target);
    });

    init();
});
