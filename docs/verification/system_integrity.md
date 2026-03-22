# System Integrity Verification

## ecosystem_doctor_integrity

目的  
Ecosystem 全体の整合性を確認する

検査内容

・主要ディレクトリの存在確認  
・制度関連構造の検証  
・研究関連構造の検証


## ecosystem_structure_scan

目的  
Ecosystem のディレクトリ構造が設計仕様と一致することを確認する

検査内容

・主要 repository 構造  
・研究関連ディレクトリ  
・制度関連ディレクトリ


## canon_directory_integrity

目的  
制度記録領域 canon の整合性を確認する

検査内容

・canon ディレクトリの存在  
・制度記録ファイルの配置  
・制度履歴の欠落確認


## artifact_directory_integrity

目的  
研究成果物領域 artifact の整合性を確認する

検査内容

・artifact ディレクトリの存在  
・成果物保存構造の検証  
・保存パスの整合性


## repo_entrypoints_present

目的  
各 repository に入口ドキュメントが存在することを確認する

検査内容

・README 等の存在  
・入口導線の確認


## repo_git_clean_check

目的  
Git 状態が再現可能であることを確認する

検査内容

・未コミット変更の確認  
・working tree 状態確認


## repo_license_presence

目的  
公開条件の明示を確認する

検査内容

・LICENSE ファイルの存在  
・公開条件の確認

