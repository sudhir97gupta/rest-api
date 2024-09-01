const apiUrl = "http://127.0.0.1:5000";

// Function to get all items
function getItems() {
    fetch(`${apiUrl}/get_items`)
        .then(response => response.json())
        .then(data => {
            const itemList = document.getElementById('item-list');
            itemList.innerHTML = ''; // Clear previous items
            data.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.className = 'item';
                itemDiv.innerHTML = `<strong>${item["Item-Name"]}</strong>: $${item["Price"]}`;
                itemList.appendChild(itemDiv);
            });
        })
        .catch(error => console.error('Error fetching items:', error));
}

// Function to add a new item
document.getElementById('add-item-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const itemName = document.getElementById('item-name').value;
    const itemPrice = document.getElementById('item-price').value;

    fetch(`${apiUrl}/add_item`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "Item-Name": itemName,
            "Price": itemPrice
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        getItems(); // Refresh the list
    })
    .catch(error => console.error('Error adding item:', error));
});

// Function to update an item
document.getElementById('update-item-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const itemName = document.getElementById('update-item-name').value;
    const itemPrice = document.getElementById('update-item-price').value;

    fetch(`${apiUrl}/update_item`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "Item-Name": itemName,
            "Price": itemPrice
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        getItems(); // Refresh the list
    })
    .catch(error => console.error('Error updating item:', error));
});

// Function to get a specific item by name
document.getElementById('get-item-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const itemName = document.getElementById('get-item-name').value;

    fetch(`${apiUrl}/get_item?Item-Name=${encodeURIComponent(itemName)}`)
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
            } else {
                alert(`Found item: ${data["Item-Name"]}, Price: $${data["Price"]}`);
            }
        })
        .catch(error => console.error('Error fetching item:', error));
});
