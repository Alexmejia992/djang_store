console.log('hola mundo')

const updateBtns = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        const productName = this.dataset.product
        const action = this.dataset.order
        // const action = this.dataset.action
        console.log(productName)
        console.log(user)
        updateUserOrder(productName, action)
    })
}

function updateUserOrder(productName, action){
    console.log('sending data...')
    const url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'productName': productName, 'action': action
        })
    }).then((response) =>{
        return response.json()
    }).then((data) =>{
        console.log('data:', data)
    })
}