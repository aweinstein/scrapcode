
in_txt = r'''\REQUIRE  $A$, $y$, stopping criterion
\STATE $x_0 =0$
\STATE $c_0 = A^Ty$
\STATE $\lambda_0, I_0 = \max_i(|c_0(i)|)$
\STATE $k = 0$
\WHILE{not converged}
\STATE $c_k = c_0 - A^T A x$
\STATE $d_k = \vc{0}$
\STATE $d_k(I_k) = \left(A_{I_k}^T A_{I_k})^{-1} \sign(c_k(I_k) \right)$
\STATE $\gamma_k^+, i_k^+ = \min_{i \in I^c}^+ \left\{
  \frac{\lambda_k - c_k(i)}{1 - a_i^TA_Id_k(I)},
  \frac{\lambda_k + c_k(i)}{1 + a_i^TA_Id_k(I)}
  \right\}$
\STATE $\gamma_k^-, i_k^- = \min_{i \in I}^+\left\{ -x_k(i) / d_k(i) \right\}$
\IF{$\gamma_k^+ < \gamma_k^-$}
\STATE $\gamma_k = \gamma_k^+$
\STATE $I_{k+1} = I_k \cup \{i_k^+\}$
\ELSE
\STATE $\gamma_k = \gamma_k^-$
\STATE $I_{k+1} = I_k \backslash \{i_k^-\}$
\ENDIF
\STATE $x_{k+1} = x_k + \gamma_k d_k$
\STATE $\lambda_{k+1} = \lambda_k - \gamma_k$
\STATE $k = k + 1$
\ENDWHILE
\ENSURE $x_j, \lambda_j$ for $j = 1, \ldots, k$'''

r_list = {'REQUIRE': 'Require',
          'ENSURE': 'Ensure',
          'STATE': 'State',
          'WHILE': 'While',
          'ENDWHILE': 'EndWhile',
          'IF': 'If',
          'ENDIF': 'EndIf',
          'ELSE': 'Else',
          'REPEAT': 'Repeat',
          'UNTIL': 'Until',
          'FOR': 'For',
          'ENDFOR': 'EndFor',
          'END': 'End',
          '\OR': 'OR',
          }

out_txt = in_txt
for k,v in r_list.iteritems():
    print 'Replacing %s by %s' % (k, v)
    out_txt = out_txt.replace(k, v)

print out_txt
