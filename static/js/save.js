function savePDF() {
    const formData = new FormData(document.getElementById('uploadForm'));
    formDataTest = document.getElementById('uploadForm');
    formDataTest.classList.remove('error-border');



    console.log("begin pdf register");
    fetch('/registerPDF', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch(error => {
            console.error('Error:', error);s
        });

}



