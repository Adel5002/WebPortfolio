let icon = document.getElementById("icon")

if (!localStorage.theme) localStorage.theme = "light"
document.body.className = localStorage.theme
if(document.body.classList.contains("dark")) {
        icon.src = "/static/images/sun.png";
    }else{
        icon.src = "/static/images/moon.png";
    }

toggleThemeBtn.onclick = () => {
    document.body.classList.toggle("dark")
    if(document.body.classList.contains("dark")) {
        icon.src = "/static/images/sun.png";
    }else{
        icon.src = "/static/images/moon.png";
    }
    localStorage.theme = document.body.className || "light"
}