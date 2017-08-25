window.onload = function() {
    const socket = io('http://' + document.domain + ':' + location.port);
    socket.on('connect', () => {

        let buttons = document.getElementsByClassName('OnOff')
        for (var i = buttons.length - 1; i >= 0; i--) {
            buttons[i].addEventListener('click', (e) => {
                let that = e.target
                let pin = that.getAttribute('data-pin')
                if (that.checked) {
                	socket.emit('onPin', pin)
                } else {
                    socket.emit('offPin', pin)
                }
            }, false)
        }

        console.log(socket.id)
    });
}