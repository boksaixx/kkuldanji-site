-- 꿀단지 Supabase 스키마
-- Supabase 대시보드 → SQL Editor 에 통째로 붙여넣고 Run 한 번이면 끝.

create table if not exists members (
  id uuid primary key,
  name text not null,
  team text not null,
  device text,
  created_at timestamptz default now()
);

create table if not exists reads (
  id bigserial primary key,
  member_id uuid references members(id),
  name text, team text,
  issue_no int,
  path text,
  is_new boolean default false,
  created_at timestamptz default now()
);

create table if not exists votes (
  id bigserial primary key,
  member_id uuid references members(id),
  name text, team text,
  issue_no int,
  choice text,
  reason text,
  created_at timestamptz default now()
);

create table if not exists feedback (
  id bigserial primary key,
  member_id uuid references members(id),
  name text, team text,
  issue_no int,
  choice text,
  reason text,
  created_at timestamptz default now()
);

-- 보안: 브라우저(anon 키)는 "쓰기만" 가능, 읽기는 대시보드에서만.
alter table members  enable row level security;
alter table reads    enable row level security;
alter table votes    enable row level security;
alter table feedback enable row level security;

create policy "anon insert members"  on members  for insert to anon with check (true);
create policy "anon insert reads"    on reads    for insert to anon with check (true);
create policy "anon insert votes"    on votes    for insert to anon with check (true);
create policy "anon insert feedback" on feedback for insert to anon with check (true);

-- 보기 편한 뷰 (대시보드 Table Editor에서 확인)
create or replace view v_readers as
select m.name, m.team, m.created_at as joined,
       count(r.id) as reads, max(r.created_at) as last_seen,
       count(distinct r.issue_no) as issues_read
from members m left join reads r on r.member_id = m.id
group by m.id, m.name, m.team, m.created_at
order by last_seen desc nulls last;

create or replace view v_issue_stats as
select issue_no,
       count(distinct member_id) as unique_readers,
       count(*) as total_opens
from reads where issue_no is not null
group by issue_no order by issue_no desc;

create or replace view v_vote_results as
select issue_no, choice, count(*) as n
from votes group by issue_no, choice order by issue_no desc, n desc;
