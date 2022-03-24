  $(document).ready(function() {
    $(".login").click(function() {
        $(".signup").hide();
        $(".log").show();
    });
  });


  $(document).ready(function() {
    $(".titlephotography").hide();
    $(".titlepainting").hide();
    $(".titleembroidery").hide();
    $(".titlefashion").hide();
  });

  $(document).ready(function() {
    $("#photography").click(function(){
        console.log('............')
        document.getElementById('photography').style.backgroundColor = '#C79E17';
        document.getElementById('painting').style.backgroundColor = '';
        document.getElementById('embroidery').style.backgroundColor = '';
        document.getElementById('fashion design').style.backgroundColor = '';
        $(".art").hide();
        $(".artphotography").show();
        $(".titlephotography").show();
        $(".titlepainting").hide();
        $(".titleembroidery").hide();
        $(".titlefashion").hide();
    });
  });

  $(document).ready(function() {
    $("#painting").click(function(){
        console.log('............')
        document.getElementById('photography').style.backgroundColor = '';
        document.getElementById('painting').style.backgroundColor = '#C79E17';
        document.getElementById('embroidery').style.backgroundColor = '';
        document.getElementById('fashion design').style.backgroundColor = '';
        $(".art").hide();
        $(".artpainting").show();
        $(".titlephotography").hide();
        $(".titlepainting").show();
        $(".titleembroidery").hide();
        $(".titlefashion").hide();
    });
  });

  $(document).ready(function() {
    $("#embroidery").click(function(){
        console.log('............')
        document.getElementById('photography').style.backgroundColor = '';
        document.getElementById('painting').style.backgroundColor = '';
        document.getElementById('embroidery').style.backgroundColor = '#C79E17';
        document.getElementById('fashion design').style.backgroundColor = '';
        $(".art").hide();
        $(".artembroidery").show();
        $(".titlephotography").hide();
        $(".titlepainting").hide();
        $(".titleembroidery").show();
        $(".titlefashion").hide();
    });
  });

  $(document).ready(function() {
    $(".fashion").click(function(){
        console.log('............')
        document.getElementById('photography').style.backgroundColor = '';
        document.getElementById('painting').style.backgroundColor = '';
        document.getElementById('embroidery').style.backgroundColor = '';
        document.getElementById('fashion design').style.backgroundColor = '#C79E17';
        $(".art").hide();
        $(".artfashion").show();
        $(".titlephotography").hide();
        $(".titlepainting").hide();
        $(".titleembroidery").hide();
        $(".titlefashion").show();
    });
  });

  $(document).ready(function() {
    $(".change").click(function() {
        $(".form").toggle();
    });
  });

  $(document).ready(function() {
    $(".sign").click(function() {
        $(".log").hide();
        $(".signup").show();
  
    });
  });
  
  $(document).ready(function() {
    $(".click").click(function() {
        $(".log").hide();
        $(".reset").show();
  
    });
  });
  $(document).ready(function() {
    $(".done").click(function() {
        $(".reset").hide();
        $(".codeNumber").show();
  
    });
  });
  
  $(document).ready(function() {
    $(".done2").click(function() {
        $(".codeNumber").hide();
        $(".returnPassword").show();
  
    });
  });
  $(function() {
  
  
    $(window).on("scroll", function() {
        var sc = $(window).scrollTop();
        if (sc > 100) {
            $(".navbar").css("backgroundColor", "#000");
        } else {
            $(".navbar").css("backgroundColor", "transparent");
        }
    })
  })

  $(document).ready(function() {
    $(".artPhoto").click(function() {
        $(".artWork").show();
        $(".about").hide();
        $(".artPhoto").css("backgroundColor", "#232123");
        $(".artPhoto").css("color", "#D4AF37");
        $(".aboutUser").css("backgroundColor", "transparent");
    });
  });
  
  $(document).ready(function() {
    $(".aboutUser").click(function() {
        $(".artWork").hide();
        $(".artPhoto").css("backgroundColor", "transparent");
        $(".about").show();  
    });
  });
  


  $(document).ready(function() {
    $(".okkk").click(function() {
        $(".addWork").hide();
        $(".site-footer").hide();
        $(".successfully").show();
  
    });
  });
  
  $(document).ready(function() {
    $(".fashionDesign").click(function() {
        $(".fa").show();
    });
  });
  
  

  $(window).on("scroll", function() {
    var sc = $(window).scrollTop();
    if (sc > 450) {
        $(".brief1").fadeIn("slow");
    }
    if (sc > 850) {
        $(".brief2").fadeIn("slow");
    }
    if (sc > 1600) {
        $(".brief3").fadeIn("slow");
    }
    if (sc > 2400) {
        $(".brief4").fadeIn("slow");
    } else {
        $(".brief1").css("backgroundColor", "#000");
    }
})



// community
// $(document).ready(function() {
//   $(".move").click(function() {
//       $(".choose").hide();
  
//       $(".chat").show();
//   })
// })

const messages = document.getElementById('messages');

function appendMessage() {
	const message = document.getElementsByClassName('message')[0];

  messages.appendChild(newMessage);
}

function getMessages() {

  shouldScroll = messages.scrollTop + messages.clientHeight === messages.scrollHeight;
  
  appendMessage();

  if (!shouldScroll) {
    scrollToBottom();
  }
}

function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
}

scrollToBottom();

setInterval(getMessages, 100);

$(document).ready(function() {
    $(".move").click(function() {
        $(".choose").hide();
    
        $(".chat").fadeIn(function scrollToBottom() {
            messages.scrollTop = messages.scrollHeight;
          }
          );
    })
})



  
    AOS.init({
        offset: 400,
    duration: 1000
    });



