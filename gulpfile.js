const gulp = require('gulp');
const gs = require('gulp-selectors');
const cleanCSS = require('gulp-clean-css');
const htmlmin = require('gulp-htmlmin');
const { parallel } = require('gulp');

function condense () {
    return gulp.src(['src/index.css', 'src/index.html'])
        .pipe(gs.run())
        .pipe(htmlmin({ collapseWhitespace: true, collapseInlineTagWhitespace: true }))
        // .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest('dist'));
}

function superClean () {

    return gulp.src('dist/index.css')
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest('dist'));
}

exports.default = condense