async function loadProducts() {
    const response = await fetch('http://localhost:5000/products');
    const products = await response.json();
    document.getElementById("products").innerHTML = products.map(p => `<p>${p.name} - $${p.price}</p>`).join("");
}
document.addEventListener("DOMContentLoaded", loadProducts);
