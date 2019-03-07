const express = require('express');
const next = require('next');
const httpProxy = require('http-proxy');
const cookieParser = require('cookie-parser');

const DEV = process.env.NODE_ENV !== 'production';
const APP = next({ DEV });
const handle = APP.getRequestHandler();

const PROXY = httpProxy.createProxyServer({
    target: 'http://' + process.env.DJANGO_HOST + ':' + process.env.DJANGO_PORT,
    ws: true
});

APP.prepare().then(() => {
    const SERVER = express()
    SERVER.enable('trust proxy');
    SERVER.use(cookieParser());

    SERVER.get('/api*', (req, res) => {
        return PROXY.web(req, res, { target: 'http://' + process.env.DJANGO_HOST + ':' + process.env.DJANGO_PORT });
    });

    SERVER.get('/admin*', (req, res) => {
        return PROXY.web(req, res, { target: 'http://' + process.env.DJANGO_HOST + ':' + process.env.DJANGO_PORT });
    });

    SERVER.get('*', (req, res) => {
        return handle(req, res);
    });

    SERVER.listen(process.env.PORT);
    console.log(`Node listening at port ${process.env.NODE_ENV}.`);
});
