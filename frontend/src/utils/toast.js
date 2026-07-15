function show(message, type = "success") {

    window.dispatchEvent(
        new CustomEvent("toast", {
            detail: {
                message,
                type
            }
        })
    );

}

export default {

    success(message) {
        show(message, "success");
    },

    error(message) {
        show(message, "error");
    },

    warning(message) {
        show(message, "warning");
    },

    info(message) {
        show(message, "info");
    }

};