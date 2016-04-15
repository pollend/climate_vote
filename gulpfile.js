var gulp = require('gulp');
var ts = require('gulp-typescript');

gulp.task('typescript', function () {
	return gulp.src('resource/typescript/**/*.ts')
		.pipe(ts({
			"target": "ES5",
			"module": "system",
			"moduleResolution": "node",
			"sourceMap": true,
			"emitDecoratorMetadata": true,
			"experimentalDecorators": true,
			"removeComments": true,
			"noImplicitAny": false
		}))
		.pipe(gulp.dest('src/app/static/typescript'));
});