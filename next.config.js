//js
module.exports = () => {
    const rewrites = () => {
        return [
            {
                source: "/cats",
                destination: "https://meowfacts.herokuapp.com",
            },
            {
                source: "/time",
                destination: "http://127.0.0.1:5000/time",
            },
        ];
    };
    return {
        rewrites,
    };
};
