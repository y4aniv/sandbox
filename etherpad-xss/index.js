var unpack = (cs) => {
    const headerRegex = /Z:([0-9a-z]+)([><])([0-9a-z]+)|/;
    const headerMatch = headerRegex.exec(cs);
    if ((!headerMatch) || (!headerMatch[0])) error(`Not a changeset: ${cs}`);
    const oldLen = parseInt(headerMatch[1], 36);
    const changeSign = (headerMatch[2] === '>') ? 1 : -1;
    const changeMag = parseInt(headerMatch[3], 36)
    const newLen = oldLen + changeSign * changeMag;
    const opsStart = headerMatch[0].length;
    let opsEnd = cs.indexOf('$');
    if (opsEnd < 0) opsEnd = cs.length;
    return {
        oldLen,
        newLen,
        ops: cs.substring(opsStart, opsEnd),
        charBank: cs.substring(opsEnd + 1),
    };
};

class Op {
    /**
     * @param {(''|'='|'+'|'-')} [opcode=''] - Initial value of the `opcode` property.
     */
    constructor(opcode = '') {
      /**
       * The operation's operator:
       *   - '=': Keep the next `chars` characters (containing `lines` newlines) from the base
       *     document.
       *   - '-': Remove the next `chars` characters (containing `lines` newlines) from the base
       *     document.
       *   - '+': Insert `chars` characters (containing `lines` newlines) at the current position in
       *     the document. The inserted characters come from the changeset's character bank.
       *   - '' (empty string): Invalid operator used in some contexts to signifiy the lack of an
       *     operation.
       *
       * @type {(''|'='|'+'|'-')}
       * @public
       */
      this.opcode = opcode;
  
      /**
       * The number of characters to keep, insert, or delete.
       *
       * @type {number}
       * @public
       */
      this.chars = 0;
  
      /**
       * The number of characters among the `chars` characters that are newlines. If non-zero, the
       * last character must be a newline.
       *
       * @type {number}
       * @public
       */
      this.lines = 0;
  
      /**
       * Identifiers of attributes to apply to the text, represented as a repeated (zero or more)
       * sequence of asterisk followed by a non-negative base-36 (lower-case) integer. For example,
       * '*2*1o' indicates that attributes 2 and 60 apply to the text affected by the operation. The
       * identifiers come from the document's attribute pool.
       *
       * For keep ('=') operations, the attributes are merged with the base text's existing
       * attributes:
       *   - A keep op attribute with a non-empty value replaces an existing base text attribute that
       *     has the same key.
       *   - A keep op attribute with an empty value is interpreted as an instruction to remove an
       *     existing base text attribute that has the same key, if one exists.
       *
       * This is the empty string for remove ('-') operations.
       *
       * @type {string}
       * @public
       */
      this.attribs = '';
    }
  
    toString() {
      if (!this.opcode) throw new TypeError('null op');
      if (typeof this.attribs !== 'string') throw new TypeError('attribs must be a string');
      const l = this.lines ? `|${exports.numToString(this.lines)}` : '';
      return this.attribs + l + this.opcode + exports.numToString(this.chars);
    }
  }

var deserializeOps = function* (ops) {
    const regex = /((?:\*[0-9a-z]+)*)(?:\|([0-9a-z]+))?([-+=])([0-9a-z]+)|(.)/g;
    let match;
    while ((match = regex.exec(ops)) != null) {
        if (match[5] === '$') return; // Start of the insert operation character bank.
        if (match[5] != null) error(`invalid operation: ${ops.slice(regex.lastIndex - 1)}`);
        const op = new Op(match[3]);
        op.lines = parseInt(match[2] || '0', 36);
        op.chars = parseInt(match[4], 36)
        op.attribs = match[1];
        yield op;
    }
};

var unpacked = unpack("Z:34<2w-33*0*1*2*3+1*0+6$*couocu")
var ops = [...deserializeOps(unpacked.ops)]

console.log("[DEBUG] unpacked: ", unpacked)
console.log("[DEBUG] ops: ", ops)