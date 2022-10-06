let buttonarray= document.querySelectorAll("div.publi_buttons button");

let sectionarray= document.querySelectorAll("div.section");
// console.log(buttonarray);
// console.log(sectionarray);

for (let index = 0; index < buttonarray.length; index++) {
    buttonarray[index].addEventListener("click",function(){
        console.log("hi ...");
        for (let i = 0; i < sectionarray.length; i++) {
            // const element = array[index];
        
                if(i!=index){
                    // sectionarray[i].style.display="none";
                    sectionarray[i].classList.add("sectionunclick");
                    sectionarray[i].classList.remove("sectionclick");

                }
                else{
                    // sectionarray[index].style.display="flex";
                    sectionarray[index].classList.add("sectionclick");
                    sectionarray[i].classList.remove("sectionunclick");

                }
                
                
        
        }
      
        
    })
    
}


