"use strict";
const path = require("path");
const { promisify } = require("util");
const childProcess = require("child_process");
const { chmod } = require("fs");
const exec = promisify(childProcess.exec);

const bin = path.join(__dirname, "../guess");

console.log("---------------- changing permissions");
chmod(bin, "777", (e) => {
  console.log(e);
});

module.exports = async (input) => {
  console.log("input", input);
  console.log("bin", bin);
  try {
    const { stderr, stdout } = await exec(`echo '${input}' | ${bin}`);
    let result = stdout && stdout.toString().split(":");
    result = result[result.length - 1].trim();
    console.log("result", result);
    return result;
  } catch (e) {
    console.log("ERROR", e);
  }
};

// module.exports.sync = () =>
//   parseMac(childProcess.execFileSync(bin, { encoding: "utf8" }));
