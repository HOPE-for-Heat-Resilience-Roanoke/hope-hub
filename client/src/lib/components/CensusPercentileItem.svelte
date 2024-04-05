<script>
  export let value;

  function getNumberWithOrdinal(n) {
    var s = ["th", "st", "nd", "rd"],
        v = n % 100;
    return (s[(v - 20) % 10] || s[v] || s[0]);
  }
  const format = (number) => parseInt((number * 100).toLocaleString(undefined, {minimumFractionDigits: 0}));

  const callout = (number) => number > 0.899999999999;
</script>

<span class:callout={callout(value)}>{format(value)}<sup>{getNumberWithOrdinal(format(value))}</sup> percentile</span>
