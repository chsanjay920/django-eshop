$(document).ready(function() {
    $('#add-to-cart-btn').click(function() {
      var productId = 'adjustable-wrench'; // Replace with the actual product ID
      var quantity = $('#quantity-input').val();
      addToCart(productId, quantity);
    });
  });
  

// Add product to cart
function addToCart(productId, quantity) {
    $.ajax({
      url: '/cart/add/',
      type: 'POST',
      data: {
        'product_id': productId,
        'quantity': quantity
      },
      success: function(response) {
        // Update cart display
        updateCartDisplay(response);
      },
      error: function(xhr, status, error) {
        console.log('Error adding product to cart:', error);
      }
    });
  }
  
  // Remove product from cart
  function removeFromCart(productId) {
    $.ajax({
      url: '/cart/remove/',
      type: 'POST',
      data: {
        'product_id': productId
      },
      success: function(response) {
        // Update cart display
        updateCartDisplay(response);
      },
      error: function(xhr, status, error) {
        console.log('Error removing product from cart:', error);
      }
    });
  }
  
  // Update cart display
  function updateCartDisplay(cartData) {
    // Update subtotal, tax, and total
    $('#subtotal').text(cartData.subtotal);
    $('#tax').text(cartData.tax);
    $('#total').text(cartData.total);
    
    // Update cart table
    $('#cart-table').empty();
    $.each(cartData.items, function(index, item) {
      var row = '<tr>' +
                  '<td>' +
                    '<div class="cartinformation">' +
                      '<img src="' + item.image_url + '">' +
                      '<div>' +
                        '<p>' + item.name + '</p>' +
                        '<small>Price: £' + item.price.toFixed(2) + '</small>' +
                        '<br>' +
                        '<a href="#" onclick="removeFromCart(' + item.id + ')">Remove</a>' +
                      '</div>' +
                    '</div>' +
                  '</td>' +
                  '<td><input type="number" value="' + item.quantity + '" onchange="updateCartItem(' + item.id + ', this.value)"></td>' +
                  '<td>£' + item.subtotal.toFixed(2) + '</td>' +
                '</tr>';
      $('#cart-table').append(row);
    });
  }
  
  // Update cart item quantity
  function updateCartItem(productId, quantity) {
    $.ajax({
      url: '/cart/update/',
      type: 'POST',
      data: {
        'product_id': productId,
        'quantity': quantity
      },
      success: function(response) {
        // Update cart display
        updateCartDisplay(response);
      },
      error: function(xhr, status, error) {
        console.log('Error updating cart item:', error);
      }
    });
  }
  