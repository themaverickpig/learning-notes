// const { imgs } = require("@vue/shared")

const imgs = document.querySelectorAll('.img')
imgs.forEach(imgs => {
  imgs.addEventListener('click',()=>{
    removeActiveClasses()
    imgs.classList.add('active')
  })
})

function removeActiveClasses(){
  imgs.forEach(imgs =>{
    imgs.classList.remove('active')
  })
}