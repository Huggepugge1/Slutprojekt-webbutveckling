function calculate() {
    let EDD = document.getElementById("EDD").value;
    let fd = document.getElementById("fd").value;
    let preg = document.getElementById("preg").value;
    const divisor = 86400000
    let normal = 280;
    let calcEDD = EDD.split(" ").map(str => Number(str));
    let calcFD = fd.split(" ").map(str => Number(str));
    let calcPreg = preg.trim().split("+").map(str => Number(str));
    if (EDD && fd) {
        let date1 = new Date(calcFD[0], calcFD[1] - 1, calcFD[2]);
        let date2 = new Date(calcEDD[0], calcEDD[1] - 1, calcEDD[2]);
        let delta = (date1.getTime() - date2.getTime()) / divisor;
        document.getElementById("output").value = `${Math.floor((normal + delta) / 7)} + ${(normal + delta) % 7}`;
    } else if (EDD && preg) {
        let offset = ((calcPreg[0] * 7) + calcPreg[1]) - normal;
        let EDD = new Date(calcEDD[0], calcEDD[1] - 1, calcEDD[2]);
        console.log(EDD, offset, calcPreg);
        document.getElementById("output").value = `${new Date(EDD.setDate(EDD.getDate() + offset)).toDateString()}`;
    } // else if (fd != -1) {
    //     offset = normal - ((pregnancy[0] * 7) + pregnancy[1])
    //     fd = datetime.date(fd[0], fd[1], fd[2])
    //     print(f 'Calculated at: {fd + datetime.timedelta(offset)}')
    // }
}