%
% tboege-preprint.sty - Tobias Boege's preprint settings
% (C) 2021 Tobias Boege <post@taboege.de>
%
% This is free software; you can redistribute it and/or
% modify it under the terms of the Artistic License 2.0.
%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tboege-preprint}[2021/12/27 v1.1 Tobias Boege's preprint settings]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{amsart}}
\ProcessOptions\relax
\LoadClass[11pt, a4paper]{amsart}

\renewcommand{\datename}{\textit{Date}:}

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}

\RequirePackage[indent]{parskip}

\RequirePackage[margin=2.5cm, headheight=13pt, headsep=13pt]{geometry}
\RequirePackage{fancyhdr}
% Page number alternating on left and right header, no footer
\fancypagestyle{pagetoplr}{%
  \fancyhf{}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
  \fancyhead[RO,LE]{\footnotesize\fancyplain{}{\thepage}}%
}
\pagestyle{pagetoplr}
% Really, no footer. \maketitle sets \thispagestyle{plain},
% but this switches it to completely empty.
\RequirePackage{etoolbox}
\apptocmd{\maketitle}{\thispagestyle{empty}}{}{}

% https://tex.stackexchange.com/a/560609
\makeatletter
\patchcmd{\@setaddresses}{\indent}{\noindent}{}{}
\patchcmd{\@setaddresses}{\indent}{\noindent}{}{}
\patchcmd{\@setaddresses}{\indent}{\noindent}{}{}
\patchcmd{\@setaddresses}{\indent}{\noindent}{}{}
\makeatother

% Short note sectioning format
%\RequirePackage{titlesec}
%\titleformat{\section}[runin]
%{\normalfont\normalsize\bfseries}{§\thesection}{1ex}{}[.]
%
%\titleformat{\subsection}[runin]
%{\normalfont\normalsize\bfseries}{§\thesubsection}{1ex}{}[.]

\RequirePackage{microtype}
\RequirePackage{amsfonts,amssymb}
\RequirePackage{amsthm,amsmath}
\RequirePackage{mathtools}
\RequirePackage{textcomp}
\RequirePackage{xfrac}
\RequirePackage{xspace}
% Short \bm command for bold math symbol
\RequirePackage{bm}
\RequirePackage[mathscr]{eucal}
\RequirePackage[inline]{enumitem}

% paralist
\newlist{paraenum}{enumerate}{1}
\setlist[paraenum]{wide, label=(\arabic*)}
\newlist{inparaenum}{enumerate*}{1}
\setlist[inparaenum]{label=(\arabic*)}

% Symmetrical margins on lists
\setlist[itemize]{leftmargin=4em, rightmargin=4.5em, label=---}
\setlist[enumerate]{leftmargin=4em, rightmargin=4.5em}
\setlist[description]{leftmargin=4em, labelindent=4em, rightmargin=4.5em}

% Bold text includes bold math, in particular in section headers.
% https://tex.stackexchange.com/a/124311
\makeatletter
\g@addto@macro\bfseries{\boldmath}
\makeatother

\RequirePackage{graphicx}
\RequirePackage{url}
\RequirePackage{xcolor}

\definecolor{darkred}{RGB}{160,0,0}
\definecolor{darkblue}{RGB}{0,0,160}

\RequirePackage{hyperref}
\RequirePackage[sort]{cleveref}
\hypersetup{
  colorlinks,
  citecolor=darkred,
  filecolor=black,
  linkcolor=darkblue,
  urlcolor=darkblue
}

\RequirePackage{stmaryrd}
\newcommand{\lsem}{\llbracket}
\newcommand{\rsem}{\rrbracket}
% https://tex.stackexchange.com/a/154548
\newcommand{\CIperp}{\mathrel{\text{$\perp\mkern-10mu\perp$}}}
\newcommand{\CIS}[1]{\lsem#1\rsem}

% Smart Studený-/Sturmfels-style CI statement:
%   \CI{I,J}   -> [I _ J]
%   \CI{I,J|K} -> [I _ J | K]
%   \CI{I|K}   -> [I _ I | K]
\RequirePackage{ifthen}
\RequirePackage{listofitems}
\newcommand{\CI}[1]{{%
  \setsepchar{{:}/{|}/{,}}
  \ignoreemptyitems
  \readlist*\mylist{#1}
  \ifthenelse{\listlen\mylist[] = 2}{\mylist[2]}{}%
  [\mylist[1,1,1] \CIperp \ifthenelse{\listlen\mylist[1,1] = 2}{\mylist[1,1,2]}{\mylist[1,1,1]}%
  \ifthenelse{\listlen\mylist[1] = 2}{{} \mid \mylist[1,2]}{}]%
}}

% "Combinatorial" CI symbol macro:
%   \I{ij|K} -> (ij|K)
\newcommand{\I}[1]{{(#1)}}

\RequirePackage{xparse}
\newcommand{\CIdOp}{\triangle}
\newcommand{\CIzOp}{\raisebox{0.2em}{\rotatebox[origin=c]{180}{\ensuremath\triangle}}}
\newcommand{\CIbOp}{\square}
\NewDocumentCommand{\CId}{mG{}}{\CIdOp #2({#1})}
\NewDocumentCommand{\CIb}{mG{}}{\CIbOp #2({#1})}

\RequirePackage{bbm}

\newcommand{\CC}[1]{\mathcal{#1}}
\newcommand{\BO}[1]{\mathbf{#1}}
\newcommand{\BB}[1]{\mathbb{#1}}
\newcommand{\BBm}[1]{\mathbbm{#1}}
\newcommand{\BBP}[1]{\BB{P#1}}
\newcommand{\FR}[1]{\mathfrak{#1}}
\newcommand{\SF}[1]{\mathsf{#1}}
\newcommand{\RM}[1]{\mathrm{#1}}
\newcommand{\TT}[1]{\text{\texttt{#1}}}
\newcommand{\SR}[1]{\mathscr{#1}}
\newcommand{\NL}[1]{\mathnormal{#1}}

\newcommand{\Pow}{\CC{P}}
\newcommand{\eps}{\varepsilon}

\DeclareMathOperator{\Adj}{adj}
\DeclareMathOperator{\Tr}{tr}
\DeclareMathOperator{\Rk}{rk}
\DeclareMathOperator{\Sgn}{sgn}
\DeclareMathOperator{\Supp}{supp}

\newcommand{\blank}{{-}}
\newcommand{\defas}{\coloneqq}
\newcommand{\asdef}{\eqqcolon}
\newcommand{\defiff}{\mathbin{:\Leftrightarrow}}
\newcommand{\iffdef}{\mathbin{\Leftrightarrow:}}

\newcommand{\set}[1]{\{#1\}}
\newcommand{\Set}[1]{\left\{\,#1\,\right\}}

\newcommand{\ideal}[1]{\langle#1\rangle}
\newcommand{\Ideal}[1]{\left\langle\,#1\,\right\rangle}

\newcommand{\into}{\hookrightarrow}
\newcommand{\onto}{\twoheadrightarrow}

\newcommand{\ol}[1]{\overline{#1}}
\newcommand{\ck}[1]{\check{#1}}
\renewcommand{\hat}[1]{\widehat{#1}}
\renewcommand{\tilde}[1]{\widetilde{#1}}
\newcommand{\co}{\SF{c}}
\newcommand{\T}{\SF{T}}
\newcommand{\op}{\SF{op}}
\newcommand{\bu}{\bullet}
\newcommand{\dual}{\rceil}

% No italics, consecutive numbering per section.
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}[section]
\newtheorem*{theorem*}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem*{corollary*}{Corollary}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{fact}[theorem]{Fact}
\newtheorem*{fact*}{Fact}
\newtheorem{example}[theorem]{Example}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{observation}[theorem]{Observation}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{question}[theorem]{Question}
\newtheorem{challenge}[theorem]{Challenge}
\newtheorem*{convention*}{Convention}

% Special named environments
\newtheorem*{namedgenthm}{\namedgenthmname}
\newcounter{namedgenthm}
\makeatletter
\newenvironment{genthm*}[1]{%
  \def\namedgenthmname{#1}%
  \refstepcounter{namedgenthm}%
  \namedgenthm\def\@currentlabel{#1}%
  % Cleveref support: https://tex.stackexchange.com/a/346255
  \cref@constructprefix{namedgenthm}{\cref@result}%
  \protected@edef\@currentlabel{#1}%
  \protected@edef\@currentlabelname{genthm}%
  \protected@edef\cref@currentlabel{%
    [namedgenthm][][\cref@result]%
    #1%
  }%
  %\label[namedgenthm]{genthm:#1}%
}
{\endnamedgenthm}
\makeatother
\crefname{namedgenthm}{}{}
\Crefname{namedgenthm}{}{}

\newcommand{\Macaulay}[1]{%
  \ifthenelse{\equal{\detokenize{#1}}{\detokenize{2}}}{}%
  {\PackageError{tboege-preprint}{Always use \protect\Macaulay2, never \protect\Macaulay\space alone}{}}%
  \texttt{Macaulay#1}\xspace}

\RequirePackage{environ}
\NewEnviron{TodoList}[1][TODO]{%
  \color{darkred}
  \textbf{#1:}
  \begin{itemize}
  \BODY
  \end{itemize}
}

\newcommand{\todo}[2][TODO]{%
  \begingroup%
  \color{darkred}%
  \textbf{#1:} #2
  \endgroup%
}
