function addToCart (course) {
  var course_id = $(course).find('.course-id').val();
  $.ajax({
    type: 'POST',
    url: '/courses/cart',
    data: { id: course_id }
  }).done(function (msg) {
    console.log(msg);
    if (msg == 'Course saved in cart') {
      var button = $(course).find('button');
      button.text('In Cart!');
      button.prop('onclick', null);
    }
  });
}

function purchaseCourses () {
  //TODO: iterate over in-cart courses, POST their ids
  alert('Thanks for shopping at Homer Learning!');
  window.location.pathname = '/';
}

$(document).ready(function () {
  var $content = $('#content');
  if (window.location.pathname === '/') {
    $content.empty();
    $.ajax({
      type: 'GET',
      url: '/courses/'
    }).done(function (courses) {
      courses.forEach(function (c) {
        var courseDiv = ['<div><img src="', c.fields.image, '" /><h2>',
        c.fields.name, '</h2><p>', c.fields.description,
        '</p><button onclick="addToCart(this.parentNode)">Add to Cart</button>',
        '<input class="course-id" type="hidden" value="', c.pk, '" /></div>'].join('');
        $content.append(courseDiv);
      });
      $.ajax({
        type: 'GET',
        url: '/courses/cart'
      }).done(function (cartCourses) {
        cartCourses.forEach(function (c) {
          var button = $('.course-id[value=' + c.pk + ']').prev();
          button.text('Already in cart');
          button.prop('onclick', null);
        });
      });
    });
  } else if (window.location.pathname.indexOf('/course-detail/') === 0) {
    alert(window.location.pathname);
  } else if (window.location.pathname === '/cart') {
    $content.empty();
    $content.append('<h1>Your cart:</h1>');
    $.ajax({
      type: 'GET',
      url: '/courses/cart'
    }).done(function (courses) {
      courses.forEach(function (c) {
        var courseDiv = ['<div><img src="', c.fields.image, '" /><h2>',
        c.fields.name, '</h2><p>', c.fields.description,
        '</p><input class="course-id" type="hidden" value="', c.pk,
        '" /></div>'].join('');
        $content.append(courseDiv);
      });
      $content.append('<button onclick="purchaseCourses()">Complete Order</button>');
    });
  }
});
