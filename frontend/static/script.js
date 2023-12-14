console.log("Works!");

const shopItems = document.getElementById('shop-items')

fetch('/items/')
.then(res => res.json())
.then(data => {
    console.log(data);

    data.forEach(item => {
        let card = document.createElement('div')
        card.classList.add('card')

        // KÉP

        let kep = document.createElement('div')
        kep.style.backgroundImage = `url(${item.image})`
        kep.classList.add('item-image')

        // CÍM

        let cim = document.createElement('h2')
        cim.innerText = item.name

        // ÁR

        let ar = document.createElement('h3')
        if(item.discount_percent == 0){
            ar.innerText = item.base_price
            ar.innerText += ' Ft'

        }else{
            ar.innerText = item.base_price * (100 - item.discount_percent) / 100
            ar.innerText += ' Ft'
            
            let old = document.createElement('span')
            old.classList.add('old-price')
            old.innerText = item.base_price
            old.innerText += ' Ft'

            ar.appendChild(old)
        }


        // AKCIÓ

        if(item.discount_percent > 0){
            let akcio = document.createElement('span')
            akcio.classList.add('discount')
            akcio.innerText = '-' + item.discount_percent + '%'
            card.appendChild(akcio)
        }

        // Kártya feltöltése alkotórészekkel
        card.appendChild(kep)
        card.appendChild(cim)
        card.appendChild(ar)

        // Kártya hozzáadása a shop-items elemhez
        shopItems.appendChild(card)
    })

})