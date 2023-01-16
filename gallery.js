function fetchGallery(mode){
    url = "galleryIMG.json";
    fetch(url).then((response) => {
        if (!response.ok){
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    }).then((json) => {
        if (mode == "gallery"){fillGallery(json)};
        if (mode == "homepage"){fillHomePage(json)};
    });
}

function fillGallery(content){
    output = "";
    content.gallery.forEach(element => {
        output += "<img src=\"./images/gallery/" + element + "\"></img>\n";
    });
    document.getElementById("gallery_output").innerHTML = output;
}

function fillHomePage(content){
    output = "";
    indecies = [];
    for (i = 0; i < 6; i++){
        while (true){
            index = Math.floor(Math.random() * content.gallery.length);
            if (!indecies.includes(index)){break;}
        }
        indecies[i] = index;
    }
    output = "";
    indecies.forEach(element => {
        output += "<img src=\"./images/gallery/" + content.gallery[element] + "\"></img>\n";
    });
    document.getElementById("homepage_output").innerHTML = output;
}