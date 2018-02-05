const path = require('path')
const webpack = require('webpack')
const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = [{
    entry: {
        'main': './resource/js/script.js',
        'style': './resource/sass/style.scss'
    },
    resolve: {
        modules: ['node_modules'],
        descriptionFiles: ['package.json'],
        extensions: ['.js', '.scss','.vue','.css']
    },
    output: {
        filename: 'js/[name].js',
        path: path.join(__dirname, 'src/app/static/')
    },
    module: {
        rules: [
            {
                test: /\.js/,
                loader: 'babel-loader!eslint-loader',
                exclude: ['/node_modules/']
            },
            {
                test: /\.scss/,
                use: ExtractTextPlugin.extract(['css-loader','resolve-url-loader','sass-loader?sourceMap=true'])
            },
            {
                test: /\.(png|jpe?g|gif|svg|woff|woff2|ttf|eot|ico)$/,
                loader: 'file-loader?name=./img/[name].[ext].'
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                  loaders: {
                    js: 'babel-loader!eslint-loader'
                  }
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('[name].css'),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            Popper: 'popper.js'
        }),
         new webpack.optimize.UglifyJsPlugin()
    ]
}];