const navItems = document.getElementsByClassName("nav__item");

window.onload = () => {
    navItems[window.sessionStorage.getItem("active")].classList.add("active");
}

for (let i = 0; i < navItems.length; i++){
    navItems[i].addEventListener("click", function(){
        let current = document.getElementsByClassName("active");
        if(current.length){
            current[0].className = current[0].className.replace(" active", "");
        }
        
        window.sessionStorage.setItem("active", i);
    })
}