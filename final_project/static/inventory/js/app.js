// Page = add_purchase.html
const purchaseForm = document.querySelector('#purchase-form');
let i = 0
var button = document.querySelector('#add-clone'+i);
// console.log(clone.children[3].id = `add-clone${i}`);

button.onclick = (e) => {
    var purchaseItemsGroup =  document.querySelector('#purchase-items'+i);
    
    let clone = purchaseItemsGroup.cloneNode(true);
    e.preventDefault();
    clone.id = `purchase-items${++i}`;
    clone.children[0].children[1].id = `product-selection${i}`;
    clone.children[2].children[1].id = `price${i}`;
    clone.children[3].setAttribute('disabled',true);
    purchaseForm.insertBefore(clone, purchaseForm.children[purchaseForm.childElementCount-1]);

}

