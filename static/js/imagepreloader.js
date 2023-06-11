
// Assuming you have a list of image names
var imageNames = ['bg_bot.jpg', 'bg_bot_repeat.jpg', 'bg_top1.jpg', 'bg_top1_repeat.gif', 'bg_top2.jpg', 'bg_top2_repeat.jpg', 'bg_top3.jpg', 'bg_top3_repeat.jpg', 'bg_top_repeat.gif', 'box2_bot.gif', 'box2_repeat.gif', 'box2_top.gif', 'box_bot.gif', 'box_repeat.gif', 'box_top.jpg', 'button1_bg.gif', 'button1_left.gif', 'button1_right.gif', 'button2_bg.gif', 'button2_left.gif', 'button2_right.gif', 'footer_logo.gif', 'icon1.jpg', 'icon2.jpg', 'icon3.jpg', 'icon4.jpg', 'icon5.jpg', 'input.gif', 'input2.gif', 'letter1.png', 'letter2.png', 'letter3.png', 'letter4.png', 'letter5.png', 'line_hor1.gif', 'line_ver1.gif', 'logo.gif', 'marker_1.gif', 'marker_2.gif', 'marker_left.jpg', 'marker_left_active.jpg', 'marker_right.jpg', 'marker_right_active.jpg', 'menu1.gif', 'menu1_active.gif', 'menu2.gif', 'menu2_active.gif', 'menu3.gif', 'menu3_active.gif', 'menu4.gif', 'menu4_active.gif', 'menu5.gif', 'menu5_active.gif', 'menu_border.gif', 'search.jpg', 'sign_up.gif', 'text.gif', 'text1.jpg', 'text2.jpg', 'text3.jpg', 'textarea.gif'];

// Array to store the image URLs
var images = [];

// Generate the image URLs dynamically
for (var i = 0; i < imageNames.length; i++) {
  var imageUrl = "/media/images/" + imageNames[i];
  images.push(imageUrl);
}

// Preload the images
preloadImages(images);
