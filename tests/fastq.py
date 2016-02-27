import unittest
from chimp.fastq import parse_fastq_lines
from io import StringIO


class FastqTests(unittest.TestCase):
    def test_parse_fastq_lines(self):
        file = StringIO(u"""@M02288:175:000000000-AHFHH:1:1101:20309:1735 1:N:0:10
GCGATAACCCGGTCGTATCGCATTCTTTACGCGAAAATAGATCGCAAATTACGAGTTTCGCTCTACAAAATTAAGGGCTATAAGTTCCCGCTTGACGTCGCGTACAGTAACTATTGACTGTATACCACTAAAGTAACGCAAGACCTTGTTCTCTTCTAGCGACCAAGGCCTGTATCAACACTACGTCCGGCCTATGGTAAGATAATCGCAAGCTGTATGACGTATTCAGGCATGTTCCGCATCTTATGCTCATTGATTCGTCGCCCACTCCGTTCAGGCGTTGGCAGCTCACTTGTAGCA
+
@BCC96CCEFFF,CEECC,6CC,,,C@,C,,,,<,<C,,,;,:,;,<,<;@CE,<C,;,;,<,,;<,;C,<@,;8,B,:,,:,<,:,C,<,,:,<,:,<,<5B,:,<,9,+,78AA+:,,:,,,9::@5,9,,9,9,99AA?CBBCC,,,++8+8,:,,,,,876@,6>+6@,>=,,,,7@,5@+5@:CECCCE=7+<++*2/**+**+1+++22:+*++3+1*/9*********/1*0(0)-473(0)*)0/)***)((/),).(.).))))-),().)).((-,43)2)-)-)))).)
@M02288:175:000000000-AHFHH:1:1101:17084:1811 1:N:0:10
TGGTTTATGAAAAATCGCAACGCACTGATGTGTTACGTATAAACTTCCGTGCTTACAGTATTGAACCATGCGGTATACATGCTCTGTTGCTCCATTAAAGTAACTAGTTGTATCGGGGATGAAAGCCGTTCCTCCGCGAACGTAGTTTTTATAAGATCGTCTAACCCTTCTGATTTGCGGGCAGAGCGACAGCCTATCCAGAGGACGGTGTGATGCATGCCGCGCGCAAACAAGGAGATCGAAGGCCTAGTGAGGTCTTTGAGGCAGAGACGTCTCCCTTGCCGGACGAGACCCCGCAAC
+
CCCCCGF9,CC,,CCFE99EAFAF9E99CAE9,CC,EACE7,,;<CEE9CEA,CC,,;;C,C,<,<CCEF,C,CEE,,C,CCEEFE9CC,,8,CB,9@B,++B,:,,,,:,,,:,:,,8@=?,,?,,:,,9,,9,,A,,AC,+,,98E,=,,9+8>+@=,EE9>,>,4,6,,6,66,@C,==,@=,@=,@@+6@+61,,,2,6+3+=7+;3+5:+;:+39*99>99@+++10******)0)2(0)0-0(+*218A))./);((./..7<)).)7)1)7).3(/(,())).).)())))()
""")
        r = list(parse_fastq_lines(file))[0]
        self.assertEqual(r.name, 'M02288:175:000000000-AHFHH:1:1101:20309:1735')
        self.assertEqual(r.region, (1, 1101))
        self.assertEqual(r.row, 1735)
        self.assertEqual(r.column, 20309)
        self.assertEqual(r.sequence, 'GCGATAACCCGGTCGTATCGCATTCTTTACGCGAAAATAGATCGCAAATTACGAGTTTCGCTCTACAAAATTAAGGGCTATAAGTTCCCGCTTGACGTCGCGTACAGTAACTATTGACTGTATACCACTAAAGTAACGCAAGACCTTGTTCTCTTCTAGCGACCAAGGCCTGTATCAACACTACGTCCGGCCTATGGTAAGATAATCGCAAGCTGTATGACGTATTCAGGCATGTTCCGCATCTTATGCTCATTGATTCGTCGCCCACTCCGTTCAGGCGTTGGCAGCTCACTTGTAGCA')
