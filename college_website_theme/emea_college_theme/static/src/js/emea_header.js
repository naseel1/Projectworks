let lastpos = 0;

// Check if the element with the "homepage" class exists
let homepageElement = document.getElementsByClassName("homepage")[0];
if (homepageElement) {
    homepageElement.addEventListener("scroll", function () {
        let wrap = homepageElement.scrollTop;
        let link_pos = document.getElementsByClassName("emea-link");
        let top_pos = document.getElementById("emea_top_menu_collapse");
        let top_bar = document.getElementById("top-items");
        let bar_pos = document.getElementById("topbar1");
        let logo_pos = document.getElementById("logo-emea");
        let name_pos = document.getElementById("logo-name");
        let span_pos = document.getElementById("logo-span");
        let pos = document.getElementsByClassName("virtual");
        let backpos = document.getElementById("top");

        if (wrap > 10) {
             for (let j = 0; j < link_pos.length; j++) {
            link_pos[j].style.color = "#000";
            link_pos[j].style.textShadow = "none";
        }
        top_pos.style.backgroundColor = "white";
        top_pos.style.height = "60px";
        top_bar.style.height = "100%";
        top_pos.style.top = "0";
        top_pos.style.left = "0px";
         top_pos.style.boxShadow = "rgba(0, 0, 0, 0.25) 3px 3px 8px 0px";
        bar_pos.style.backgroundColor = "#039990";
        bar_pos.style.height = "56px";
        logo_pos.style.height = "40px";
        logo_pos.style.margin = "0px";
        name_pos.style.fontSize = "20px";
        name_pos.style.textAlign = "left";
        span_pos.style.display = "none";
        for (let j = 0; j < pos.length; j++) {
            pos[j].style.border = "2px solid #fff";
        }
         backpos.style.background = "none";
        } else {
            for (let j = 0; j < link_pos.length; j++) {
            link_pos[j].style.color = "#fff";
            link_pos[j].style.textShadow = "#1a1919 1px 1px 7px";
        }
        top_pos.style.backgroundColor = "transparent";
        top_pos.style.height = "90px";
        top_bar.style.height = "70%";
        top_pos.style.boxShadow = "none";
        top_pos.style.top = "-10px";
        top_pos.style.left = "30px";
        bar_pos.style.backgroundColor = "transparent";
        bar_pos.style.height = "95px";
        logo_pos.style.height = "105px";
        logo_pos.style.margin = "0px 0px 0 15px";
        name_pos.style.fontSize = "34px";
        name_pos.style.textAlign = "center";
        span_pos.style.display = "block";
        for (let j = 0; j < pos.length; j++) {
            pos[j].style.border = "2px solid #039990";
        }
         backpos.style.background = "linear-gradient(180deg, rgb(0 0 0 / 54%) 0%, rgb(0 0 0 / 46%) 33%, rgb(0 0 0 / 30%) 55%, rgb(0 0 0 / 20%) 67%, rgb(0 0 0 / 0%) 100%)";
            backpos.style.height = "21vh";
        }

        lastpos = wrap;
    });
} else {
;
}
