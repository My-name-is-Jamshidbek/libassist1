const uploadFile = document.getElementById("upload-file");
const uploadBtn = document.getElementById("upload-btn");
const uploadText = document.getElementById("upload-text");

uploadBtn.addEventListener("click" , function(){
    uploadFile.click();
});

uploadFile.addEventListener("change", function() {
    if(uploadFile.value){
        uploadText.innerText = uploadFile.value;
    }else{
        uploadText.innerText = "Fayl tanlanmagan";
    }
})

