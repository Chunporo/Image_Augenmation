let fileInput = document.getElementById("file-input");
let imageContainer = document.getElementById("images");
let numOfFiles = document.getElementById("num-of-files");
let uploadButton = document.querySelector('input[type="submit"]');
let form = document.querySelector("form");

function preview(){
    imageContainer.innerHTML = "";
    numOfFiles.textContent = `${fileInput.files.length} Files Selected`;

    for(i of fileInput.files){
        let reader = new FileReader();
        let figure = document.createElement("figure");
        let figCap = document.createElement("figcaption");
        // figCap.innerText = i.name;
        figure.appendChild(figCap);
        reader.onload=()=>{
            let img = document.createElement("img");
            img.setAttribute("src",reader.result);
            figure.insertBefore(img,figCap);
        }
        imageContainer.appendChild(figure);
        reader.readAsDataURL(i);
    }

}
fileInput.addEventListener('change', preview);

form.addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from refreshing the page

    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/upload', true);
    xhr.send(new FormData(form));
});

let uploadProgress = document.getElementById('uploadProgress');

form.addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from refreshing the page

    let xhr = new XMLHttpRequest();

    xhr.upload.onprogress = function(e) {
        if (e.lengthComputable) {
            uploadProgress.value = (e.loaded / e.total) * 100;
        }
    };

    xhr.open('POST', '/upload', true);
    xhr.send(new FormData(form));
});

fileInput.addEventListener('click', function() {
    // Reset the progress bar
    uploadProgress.value = 0;
});

form.addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from refreshing the page

    let xhr = new XMLHttpRequest();

    xhr.upload.onprogress = function(e) {
        if (e.lengthComputable) {
            uploadProgress.value = (e.loaded / e.total) * 100;
        }
    };

    xhr.onload = function() {
        if (xhr.status == 200) {
            // Reset the progress bar
            uploadProgress.value = 0;
            // Download the zip file
            let a = document.createElement('a');
            a.href = window.URL.createObjectURL(xhr.response);
            a.download = 'augmented_images.zip';
            a.style.display = 'none';
            document.body.appendChild(a);
            a.click();
        }
    };

    xhr.open('POST', '/upload', true);
    xhr.responseType = 'blob'; // Expect a Blob object in response
    xhr.send(new FormData(form));
});