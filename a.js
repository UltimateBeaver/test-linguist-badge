function funcname(func) {
    if (func === undefined)
        console.log('WARNING: func undefined in astutil/funcname.');
    else if (func.id === null)
        return "anon";
    else
        return func.id.name;
}


function basename(filename) {
    if (!filename)
        return "<???>";
    var idx = filename.lastIndexOf('/');
    if (idx === -1)
        idx = filename.lastIndexOf('\\');
    return filename.substring(idx + 1);
}
