"use strict";

module.exports = (input) => {
  console.log("process.platform ", process.platform);
  if (process.platform === "darwin") {
    return require("./lib/macos")(input);
  }

  return Promise.reject(new Error("macOS only"));
};
