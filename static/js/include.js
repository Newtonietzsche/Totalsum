
function loadHTML(elementId, url)
 {
    const isElement = document.getElementById(elementId);
    if(isElement)
        {
            fetch(url)
            .then(response => response.text())
            .then(data => {document.getElementById(elementId).innerHTML = data;})
            //.catch(error => console.error('Erreur:', error));
        }
    
 }
    
loadHTML('indexHeader', '../includes/indexHeader.html');
loadHTML('header', '../includes/header.html');
loadHTML('footer', '../includes/footer.html');


