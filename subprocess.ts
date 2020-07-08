const p = Deno.run({
  cmd: ["cat", "hello.sh"],
});

await p.status();
