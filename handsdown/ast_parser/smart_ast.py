# pylint: disable=no-name-in-module
"""
Smart AST.

Provides compatibility between AST 2 and 3.
"""
import os
import sys
from typing import Any

if os.environ.get("PYTHON_VER", "3") == "3":
    if sys.version_info >= (3, 8):
        from ast import (
            AST,
            Add,
            And,
            Assign,
            AsyncFunctionDef,
            Attribute,
            Await,
            BinOp,
            BitAnd,
            BitOr,
            BitXor,
            BoolOp,
            Bytes,
            Call,
            ClassDef,
            Compare,
            Constant,
            Dict,
            DictComp,
            Div,
        )
        from ast import Ellipsis as ASTEllipsis  # pylint: disable=no-name-in-module
        from ast import (
            Eq,
            FloorDiv,
            FormattedValue,
            FunctionDef,
            GeneratorExp,
            Gt,
            GtE,
            IfExp,
            Import,
            ImportFrom,
            In,
            Index,
            Invert,
            Is,
            IsNot,
            JoinedStr,
            Lambda,
            List,
            ListComp,
            LShift,
            Lt,
            LtE,
            Mod,
            Module,
            Mult,
            Name,
            NameConstant,
            NodeVisitor,
            Not,
            NotEq,
            NotIn,
            Num,
            Or,
            Pow,
            RShift,
            Set,
            SetComp,
            Slice,
            Starred,
            Str,
            Sub,
            Subscript,
            Tuple,
            UAdd,
            UnaryOp,
            USub,
            Yield,
            YieldFrom,
            alias,
            arg,
            arguments,
            comprehension,
            expr,
            get_docstring,
            keyword,
            parse,
            stmt,
        )
    else:
        from typed_ast.ast3 import (
            AST,
            Add,
            And,
            Assign,
            AsyncFunctionDef,
            Attribute,
            Await,
            BinOp,
            BitAnd,
            BitOr,
            BitXor,
            BoolOp,
            Bytes,
            Call,
            ClassDef,
            Compare,
            Constant,
            Dict,
            DictComp,
            Div,
        )
        from typed_ast.ast3 import Ellipsis as ASTEllipsis  # pylint: disable=no-name-in-module
        from typed_ast.ast3 import (
            Eq,
            FloorDiv,
            FormattedValue,
            FunctionDef,
            GeneratorExp,
            Gt,
            GtE,
            IfExp,
            Import,
            ImportFrom,
            In,
            Index,
            Invert,
            Is,
            IsNot,
            JoinedStr,
            Lambda,
            List,
            ListComp,
            LShift,
            Lt,
            LtE,
            Mod,
            Module,
            Mult,
            Name,
            NameConstant,
            NodeVisitor,
            Not,
            NotEq,
            NotIn,
            Num,
            Or,
            Pow,
            RShift,
            Set,
            SetComp,
            Slice,
            Starred,
            Str,
            Sub,
            Subscript,
            Tuple,
            UAdd,
            UnaryOp,
            USub,
            Yield,
            YieldFrom,
            alias,
            arg,
            arguments,
            comprehension,
            expr,
            get_docstring,
            keyword,
            parse,
            stmt,
        )
else:
    from typed_ast.ast27 import (
        AST,
        Add,
        And,
        Assign,
        Attribute,
        BinOp,
        BitAnd,
        BitOr,
        BitXor,
        BoolOp,
        Call,
        ClassDef,
        Compare,
        Dict,
        DictComp,
        Div,
    )
    from typed_ast.ast27 import Ellipsis as ASTEllipsis  # pylint: disable=no-name-in-module
    from typed_ast.ast27 import (
        Eq,
        FloorDiv,
        FunctionDef,
        GeneratorExp,
        Gt,
        GtE,
        IfExp,
        Import,
        ImportFrom,
        In,
        Index,
        Invert,
        Is,
        IsNot,
        Lambda,
        List,
        ListComp,
        LShift,
        Lt,
        LtE,
        Mod,
        Module,
        Mult,
        Name,
        NodeVisitor,
        Not,
        NotEq,
        NotIn,
        Num,
        Or,
        Pow,
        RShift,
        Set,
        SetComp,
        Slice,
        Str,
        Sub,
        Subscript,
        Tuple,
        UAdd,
        UnaryOp,
        USub,
        Yield,
        alias,
        arguments,
        comprehension,
        expr,
        get_docstring,
        keyword,
        parse,
        stmt,
    )

    arg = Any
    Bytes = Any
    Constant = Str
    NameConstant = Any
    Starred = Any
    JoinedStr = Any
    FormattedValue = Any
    YieldFrom = Any
    AsyncFunctionDef = Any
    Await = Any

__all__ = [
    "Add",
    "alias",
    "And",
    "arg",
    "arguments",
    "Assign",
    "AST",
    "AsyncFunctionDef",
    "Attribute",
    "Await",
    "BinOp",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolOp",
    "Bytes",
    "Call",
    "ClassDef",
    "Compare",
    "comprehension",
    "Constant",
    "Dict",
    "DictComp",
    "Div",
    "ASTEllipsis",
    "Eq",
    "expr",
    "FloorDiv",
    "FormattedValue",
    "FunctionDef",
    "GeneratorExp",
    "get_docstring",
    "Gt",
    "GtE",
    "IfExp",
    "Import",
    "ImportFrom",
    "In",
    "Index",
    "Invert",
    "Is",
    "IsNot",
    "JoinedStr",
    "keyword",
    "Lambda",
    "List",
    "ListComp",
    "LShift",
    "Lt",
    "LtE",
    "Mod",
    "Module",
    "Mult",
    "Name",
    "NameConstant",
    "NodeVisitor",
    "Not",
    "NotEq",
    "NotIn",
    "Num",
    "Or",
    "parse",
    "Pow",
    "RShift",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "stmt",
    "Str",
    "Sub",
    "Subscript",
    "Tuple",
    "UAdd",
    "UnaryOp",
    "USub",
    "Yield",
    "YieldFrom",
]
