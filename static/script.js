let cart = [];


/* Add medicine */

function addMedicine() {

    const medicineSelect =
        document.getElementById("medicine");

    const quantityInput =
        document.getElementById("quantity");


    const medicine =
        medicineSelect.value;

    const quantity =
        parseInt(quantityInput.value);


    if (medicine === "") {

        alert("Please select a medicine.");

        return;
    }


    if (quantity <= 0 || isNaN(quantity)) {

        alert("Please enter a valid quantity.");

        return;
    }


    const selectedOption =
        medicineSelect.options[
            medicineSelect.selectedIndex
        ];


    const price =
        parseFloat(
            selectedOption.dataset.price
        );


    cart.push({
        name: medicine,
        price: price,
        quantity: quantity
    });


    displayCart();


    medicineSelect.value = "";

    quantityInput.value = 1;
}


/* Display cart */

function displayCart() {

    const cartItems =
        document.getElementById("cartItems");


    if (cart.length === 0) {

        cartItems.innerHTML = `
            <tr>
                <td colspan="5" class="empty-cart">
                    No medicines added yet.
                </td>
            </tr>
        `;

        updateBill();

        return;
    }


    cartItems.innerHTML = "";


    cart.forEach((item, index) => {

        const total =
            item.price * item.quantity;


        const row = document.createElement("tr");


        row.innerHTML = `

            <td>${item.name}</td>

            <td>${item.quantity}</td>

            <td>₹${item.price.toFixed(2)}</td>

            <td>₹${total.toFixed(2)}</td>

            <td>
                <button
                    class="remove-button"
                    onclick="removeMedicine(${index})">
                    ×
                </button>
            </td>

        `;


        cartItems.appendChild(row);

    });


    updateBill();
}


/* Remove medicine */

function removeMedicine(index) {

    cart.splice(index, 1);

    displayCart();
}


/* Calculate bill */

function updateBill() {

    let subtotal = 0;


    cart.forEach(item => {

        subtotal +=
            item.price * item.quantity;

    });


    /*
       Existing project rule:
       10% discount if total > ₹200
    */

    let discount = 0;


    if (subtotal > 200) {

        discount = subtotal * 0.10;

    }


    const amountAfterDiscount =
        subtotal - discount;


    /* 5% GST */

    const gst =
        amountAfterDiscount * 0.05;


    const grandTotal =
        amountAfterDiscount + gst;


    document.getElementById("subtotal")
        .textContent =
        subtotal.toFixed(2);


    document.getElementById("discount")
        .textContent =
        discount.toFixed(2);


    document.getElementById("gst")
        .textContent =
        gst.toFixed(2);


    document.getElementById("grandTotal")
        .textContent =
        grandTotal.toFixed(2);
}


/* Generate bill */

function generateBill() {

    if (cart.length === 0) {

        alert("Please add at least one medicine.");

        return;
    }


    updateBill();


    const total =
        document.getElementById("grandTotal")
            .textContent;


    alert(
        "Bill generated successfully!\n\n" +
        "Grand Total: ₹" + total
    );
}