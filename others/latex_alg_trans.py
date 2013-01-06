
in_txt =r'''\REQUIRE  $A$, $b$, $J$, stopping criterion
\STATE \textbf{initialize:} $r^{(0)} = b$, $\Gamma^{(0)} =
  \emptyset$, $\ell = 0$
\WHILE{not converged}
\STATE
\begin{tabular}{ll}
  \textbf{match:} & $h(j) = \vnorm{A_j^T r}$, $j = 1, \ldots, J$ \\
  \textbf{identify:} & $\Gamma^{(\ell+1)} =
  \Gamma^{(\ell)} \cup \argmax_{j} h(j)$ \\
  \textbf{update:} & $x^{\ell+1} = \argmin_{z: ~ \supp(z) \subseteq
     \Gamma^{(\ell+1)}}  \|b - A z\|_2$ \\
   & $r^{\ell+1} = b - A x^{\ell + 1}$ \\
   & $\ell = \ell+1$ \\
\end{tabular}
\ENDWHILE
\ENSURE $\widehat{x} = x^{\ell} = \argmin_{z: ~ \supp(z) \subseteq
  \Gamma^{(\ell)}} \|b - A z\|_2$'''

in_txt = r'''\REQUIRE  $A$, $b$, stopping criterion
\State \textbf{initialize:} $r^{(0)} = b$, $\Gamma^{(0)} =
  \emptyset$, $\ell = 0$
\WHILE{not converged}
\STATE
\begin{tabular}{ll}
  \textbf{match:} & $h = |A^T r |$ \\
  \textbf{identify:} & $\Gamma^{(\ell+1)} =
  \Gamma^{(\ell)} \cup \argmax_{j} |h(j)|$ \\
  \textbf{update:} & $x^{\ell+1} = \argmin_{z: ~ \supp(z) \subseteq
     \Gamma^{(\ell+1)}}  \|b - A z\|_2$ \\
   & $r^{\ell+1} = b - A x^{\ell + 1}$ \\
   & $\ell = \ell+1$ \\
\end{tabular}
\ENDWHILE
\ENSURE $\widehat{x} = x^{\ell} = \argmin_{z: ~ \supp(z) \subseteq
  \Gamma^{(\ell)}} \|b - A z\|_2$'''

r_list = {'REQUIRE': 'Require',
          'ENSURE': 'Ensure',
          'STATE': 'State',
          'WHILE': 'While',
          'ENDWHILE': 'EndWhile',
          'IF': 'If',
          'ENDIF': 'EndIf'}

out_txt = in_txt
for k,v in r_list.iteritems():
    print 'Replacing %s by %s' % (k, v)
    out_txt = out_txt.replace(k, v)

print out_txt
