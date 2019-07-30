(function () {
    var Message;
  
    Message = function ({
      text: text1,
      message_side: message_side1 })
    {
      this.text = text1;
      this.message_side = message_side1;
      this.draw = () => {
        var $message;
        $message = $($('.message_template').clone().html());
        $message.addClass(this.message_side).find('.text').html(this.text);
        $('.messages').append($message);
        return setTimeout(function () {
          return $message.addClass('appeared');
        }, 0);
      };
      return this;
    };
  
    $(function () {
      var getMessageText, message_side, sendMessage;
      message_side = 'left';
      var socket = io.connect('http://192.168.1.109:5000');

      socket.on( 'connect', function() {
        socket.emit( 'my event', {
          data: 'User Connected'
        } )
          
      } )
      socket.on( 'my response', function( msg ) {
        console.log( msg );
        if(typeof msg.user_name !== "undefined"){
          message_side = 'left';
          if(msg.user_name=="user_text")
               message_side = 'right';
            sendMessage(msg.user_name.toUpperCase().bold()+": "+msg.message);
         
        }
      })

      getMessageText = function () {
        var $message_input;
        $message_input = $('.message_input');
        return $message_input.val();
      };
      sendMessage = function (text) {
        var $messages, message;
       
        $('.message_input').val('');
        $messages = $('.messages');
        message = new Message({ text, message_side });
        message.draw();
        return $messages.animate({
          scrollTop: $messages.prop('scrollHeight') },
        300);
      };
      $('.send_message').click(function (e) {
        if (getMessageText().trim() != ""){
          socket.emit( 'my event', {
            user_name : "user_text",
            message : getMessageText()
          })
        }
        return true;
      });
      $('.message_input').keyup(function (e) {
        if (e.which === 13) {// enter key
          if (getMessageText().trim() != ""){
            socket.emit( 'my event', {
              user_name : "user_text",
              message : getMessageText()
            })
          }
          return true;
        }
      });
      
  
    });
    
  
  }).call(this);
  