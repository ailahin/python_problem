const burgerPrice= 1000
let cokePrice= 30
if (burgerPrice>=500){

    cokePrice= 0
    totalPrice= burgerPrice+cokePrice
    console.log(totalPrice,"get a free coke")
}

else{
    totalPrice= burgerPrice+cokePrice
    console.log(totalPrice)
}