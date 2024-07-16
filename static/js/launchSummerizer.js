function validateForm() {
    let isValid = true;

    console.log("Validation");
    // Get form values
    const openAIKey = document.getElementById('KeyopenAI');

    openAIKey.classList.remove('error-border');


    // Validate OpenAI Key input
    if (!openAIKey.value) {
        openAIKey.classList.add('error-border');
        isValid = false;
    }
    return isValid;
}


function launchSummerize() {

    disActivateLoader();
    savePDF();
    if (validateForm()) {

        activateLoader()
        var sumType = document.getElementById('sumType').value;
        var language = document.getElementById('language').value;
        var key = document.getElementById('KeyopenAI').value;

        fetch('/createPDF?sumType=' + sumType + '&language=' + language + '&key=' + key)
            .then(response => response.json())
            .then(mots => {
                document.getElementById('Summerized').value = mots;
                disActivateLoader();
            })
            .catch(error => {
                console.error('Erreur lors de la récupération des mots:', error);
            });
    }
}