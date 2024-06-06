$(document).ready(function() {                 
    $('.increment-btn').click(function(e) {                
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function(e) {                
        e.preventDefault();

        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addToCartBtn').click(function(e) {                
        e.preventDefault();
    
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        console.log("Adding to cart - Product ID: " + product_id + " Quantity: " + product_qty); // Debugging line
    
        var csrftoken = $(this).closest('.product_data').find('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/add-to-cart/", // Make sure this URL is correct and accessible
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: csrftoken
            },
            success: function(response) {
                console.log(response);
                var messageDiv = $('.add-to-cart-message');
                messageDiv.text(response.status);
                messageDiv.fadeIn().find('.btn-close').show();
                messageDiv.removeClass('alert-danger').addClass('alert-success').fadeIn();
    
                setTimeout(function() {
                    messageDiv.fadeOut();
                }, 5000);
            },
            error: function(xhr, status, error) {
                console.error("Error: " + status + " " + error);
                var messageDiv = $('.add-to-cart-message');
                messageDiv.text("An error occurred while adding the product to the cart.");
                messageDiv.removeClass('alert-success').addClass('alert-danger').fadeIn();
    
                setTimeout(function() {
                    messageDiv.fadeOut();
                }, 3000);
            }
        });
    });
    
    



    $('.changeQuantity').click(function(e) {                
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        // Since each product might be in a different form, find the CSRF token related to this specific product
        var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-cart/",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': csrftoken // Ensure this matches how Django expects it
            },
            
            success: function(response) {
                console.log(response);
                // Assuming you have a way to show success to the user (e.g., a notification library)
                //messages.success(response.status || 'Added to cart!');
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error("Error: " + status + " " + error);
            }
        });
    });

    
    $('.delete-cart-item').click(function(e) {                
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        // Since each product might be in a different form, find the CSRF token related to this specific product
        var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-cart-item/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: csrftoken // Ensure this matches how Django expects it
            },
            
            success: function(response) {
                console.log(response);
                messages.success(response.status)
                $('.cartdata').load(location.href + " .cartdata");   // to reload the cart page
            
            }
        });  

    });    
   
});    
