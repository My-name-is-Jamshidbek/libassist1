const   nav = document.querySelector("nav"),
        navToggle = document.querySelector(".nav__toggle"),
        menuButton = document.querySelector(".menu-button"),
        bodyy = document.querySelector("#bodyy"),
        check = document.querySelector(".check");


if (localStorage.getItem("theme") == "dark") {
    bodyy.classList.add("dark");
    localStorage.setItem("theme", "dark");
    } else {
    localStorage.setItem("theme", "light");
    bodyy.classList.remove("dark");
}

if(localStorage.getItem("sidebar-open") == "open"){
    nav.classList.add("open")
    nav.classList.add("open-text")
    nav.style.transition = "width 0s ease"
}

if(bodyy.classList.contains("dark")){
    check.style.transition = "0s"
    check.style.transform = "translateX(20px)";
}else{
    check.style.transition = "0s"
    check.style.transform = "translateX(0)";
} 

navToggle.addEventListener('click',() => {
    if(nav.classList.contains("open")){
        nav.classList.remove("open")
        nav.classList.remove("open-text")
        localStorage.setItem('sidebar-open',"close")
    }else{
        nav.classList.add("open")
        setTimeout(()=>{
            nav.classList.add("open-text")
        },200)
        localStorage.setItem('sidebar-open',"open")
    }
})

check.addEventListener('click',() => {
    if(localStorage.getItem('theme') == "dark"){
        bodyy.classList.remove("dark")
        localStorage.setItem('theme',"light")
    }else{
        bodyy.classList.add("dark")
        localStorage.setItem('theme',"dark")
    }

    check.style.transition = "0.5s"

    if(bodyy.classList.contains("dark")){
        check.style.transform = "translateX(20px)";
    }else{
        check.style.transform = "translateX(0)";
    }
})