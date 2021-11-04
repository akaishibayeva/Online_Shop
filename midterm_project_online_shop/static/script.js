$(document).ready(function() {

	var path = window.location.pathname;

	if (path.includes('search')) {
		search();
	}

	// Handling create form

	$('.phone-form').submit(function(event) {

		event.preventDefault();

		$('.new-item-created').hide();
		$('.new-item-link').hide();

		// Validating

		// Validate model
		var modelInput = $('.model-input').val();

		if (!modelInput) {
			$('.model-input').siblings('.error-detection')
			.html('Model is required');
			return false;
		}

		$('.model-input').siblings('.error-detection')
			.html('');


		// Validate company
		var companyInput = $('.company-input').val();

		if (!companyInput) {
			$('.company-input').siblings('.error-detection')
			.html('Company is required');
			return false;
		}

		$('.company-input').siblings('.error-detection')
			.html('');

		// Validate image
		var imgInput = $('.img-input').val();

		if (!imgInput) {
			$('.img-input').siblings('.error-detection')
			.html('Image is required');
			return false;
		}

		$('.img-input').siblings('.error-detection')
			.html('');

		// Validate description
		var descriptionInput = $('.description-input').val();

		if (!descriptionInput) {
			$('.description-input').siblings('.error-detection')
			.html('Description is required');
			return false;
		}

		$('.description-input').siblings('.error-detection')
			.html('');

		// Validate price
		var priceInput = $('.price-input').val();

		if (!priceInput) {
			$('.price-input').siblings('.error-detection')
			.html('Price is required');
			return false;
		}

		$('.price-input').siblings('.error-detection')
			.html('');

		if (isNaN(priceInput)) {
			$('.price-input').siblings('.error-detection')
			.html('This field can only contain number');
			return false;
		}

		$('.price-input').siblings('.error-detection')
			.html('');

		// Validate year
		var yearInput = $('.year-input').val();

		if (!yearInput) {
			$('.year-input').siblings('.error-detection')
			.html('Year is required');
			return false;
		}

		$('.year-input').siblings('.error-detection')
			.html('');

		if (isNaN(yearInput)) {
			$('.year-input').siblings('.error-detection')
			.html('This field can only contain number');
			return false;
		}

		$('.year-input').siblings('.error-detection')
			.html('');

		// Validate location
		var locationInput = $('.location-input').val();

		if (!locationInput) {
			$('.location-input').siblings('.error-detection')
			.html('Location is required');
			return false;
		}

		$('.location-input').siblings('.error-detection')
			.html('');

		// End Validation

		// Parsing stores

		var stores = locationInput.split('\n');

		for (var i = 0; i < stores.length; i++) {
			var temp = stores[i].split('-');
			stores[i] = {
				'name': temp[0].trim(),
				'mark_as_deleted': false,
				'location': temp[1].trim()
			};
		}

		$.ajax({
			url: '/create_phone',
			method: 'POST',
			data: JSON.stringify({
				'model': modelInput,
				'company': companyInput,
				'picture': imgInput,
				'description': descriptionInput,
				'price': +priceInput,
				'year': +yearInput,
				'stores': stores
			}),
			success: function(response) {
				$('.new-item-created').show();
				$('.new-item-link').show();
				$('.new-item-link a').attr('href', 
					'/view/'+response['id']);
				$('.phone-form')[0].reset();
				$('.model-input').focus();
			},
			error: function(error) {
				console.log(error);
			}
		});


	});

	$('.edit').click(function(event) {

		$(event.target).hide();
		$('.price').hide();
		$('.price-input').show();
		$('.submit').show();
		$('.discard').show();

	});

	$('.discard').click(function(event) {

		window.location.replace(window.location.href);

	});

	$('.submit').click(function(event) {

		var priceInput = $('.price-input').val();

		if (!priceInput) {
			$('.price-error').html("Price is required");
			return false;
		}

		$('.price-error').html("");

		if (isNaN(priceInput)) {
			$('.price-error').html("Price should be a number");
			return false;
		}

		$('.price-error').html("");

		var phoneId = $('.phone-id').html();

		$.ajax({
			url: '/edit-price',
			method: 'POST',
			data: JSON.stringify({
				"id": +phoneId, 
				"price": +priceInput
			}),
			success: function(response) {
				window.location.replace(window.location.href);
			},
			error: function(error) {
				console.log(error);
			}
		});

	});

	$('.del-btn').click(function(event) {
		$(event.target).hide();
		$(event.target).parents('.location-item')
		.find('.undo-btn').show();
		$(event.target).parents('.location-item')
		.find('.address').hide();

		var phoneId = $('.phone-id').html();
		var temp = $(event.target).parents('.location-item')
		.find('.address').html();

		temp = temp.split('-');

		$.ajax({
			url: '/delete-store',
			method: 'POST',
			data: JSON.stringify({
				"id": phoneId,
				"name": temp[0].trim()
			}),
			success: function(response) {

			},
			error: function(error) {

			}
		});

	});

	$('.undo-btn').click(function(event) {
		$(event.target).hide();
		$(event.target).parents('.location-item')
		.find('.del-btn').show();
		$(event.target).parents('.location-item')
		.find('.address').show();

		var phoneId = $('.phone-id').html();
		var temp = $(event.target).parents('.location-item')
		.find('.address').html();

		temp = temp.split('-');

		$.ajax({
			url: '/undo-store',
			method: 'POST',
			data: JSON.stringify({
				"id": phoneId,
				"name": temp[0].trim()
			}),
			success: function(response) {

			},
			error: function(error) {

			}
		});


	});

});

// Search ajax call

function search() {

	var searchParams = new URLSearchParams(window.location.search);
	var searchquery = searchParams.get('q');

	if (searchquery) {
		$.ajax({
			url: '/search_phone',
			method: 'POST',
			data: JSON.stringify({"query": searchquery}),
			success: function(response) {

				displayPhones(response, '.phones', searchquery);
				$('.results').html(response.length + " results are found");

			},
			error: function(error) {
				console.log(error);
			}
		});
	} else {
		$('.results').html("0 results are found");
	}
}

function displayPhones(phones, container, query) {

	for (var i = 0; i < phones.length; i++) {

		var product = phones[i]['model'] + ' - ' + phones[i]['company'];

		var phone = '<div class="col">\
				  <div class="card">\
				  	<a href="/view/'+phones[i]['id']+'" class="card-img-wrapper">\
						<img src="'+phones[i]['picture']+'" class="card-img-top" alt="'+phones[i]['model']+'">\
					</a>\
					<div class="card-body">\
					  <h5 class="card-title">'+product+'</h5>\
					  <div class="price-block">\
						<p class="card-text"> $'+phones[i]['price']+'</p>\
						<a href="/view/'+phones[i]['id']+'" class="btn btn-primary">more</a>\
					  </div>\
					</div>\
				  </div>\
				</div>';
		$(container).append(phone);

		if (query) {
			$('.card-title').mark(query);
		}
	}
}



