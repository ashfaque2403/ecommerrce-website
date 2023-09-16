
    $(document).ready(function() {
        $(".js-btn-plus, .js-btn-minus").on('click', function (e) {
            e.preventDefault();

            var inputField = $(this).closest(".input-group").find("input");
            var cartItemId = inputField.data('cart-item-id');
            var currentValue = parseInt(inputField.val());
            var newValue;

            if ($(this).hasClass("js-btn-plus")) {
                newValue = currentValue + 1;
            } else if ($(this).hasClass("js-btn-minus")) {
                newValue = currentValue - 1;
                if (newValue < 1) {
                    newValue = 1; // Or handle minimum quantity logic as needed
                }
            }

            // Send AJAX request to update the quantity
            $.ajax({
                type: 'POST',
                url: '/update_quantity/',
                data: {
                    'csrfmiddlewaretoken': '{{ csrf_token }}',
                    'cart_item_id': cartItemId,
                    'new_quantity': newValue,
                },
                success: function (data) {
                    if (data.status === 'success') {
                        // Update the input field value after successful response
                        inputField.val(newValue);
                    } else {
                        // Handle error if needed
                        console.log('Error:', data.message);
                    }
                },
                error: function (_xhr, textStatus, errorThrown) {
                    // Handle error if needed
                    console.log('Error:', errorThrown);
                },
            });
        });
        });
