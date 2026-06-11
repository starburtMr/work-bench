import { BookOpen, Home } from 'lucide-react';

import { Button } from '@/components/ui/button';
import { Link } from '@/components/ui/link';
import { paths } from '@/config/paths';
import { checkLoggedIn } from '@/utils/auth';

const HomePage = () => {
  const isLoggedIn = checkLoggedIn();

  return (
    <div className="flex h-screen items-center bg-white">
      <div className="mx-auto max-w-7xl px-4 py-12 text-center sm:px-6 lg:px-8 lg:py-16">
        <h2 className="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl">
          <span className="block">Next.js App Router Toolkit</span>
        </h2>
        <img src="/logo.svg" alt="react" />
        <p>Reusable App Router skeleton for API-backed product frontends</p>
        <div className="mt-8 flex justify-center">
          <div className="inline-flex rounded-md shadow">
            <Link
              href={
                isLoggedIn
                  ? paths.app.root.getHref()
                  : paths.auth.login.getHref()
              }
            >
              <Button icon={<Home className="size-6" />}>Get started</Button>
            </Link>
          </div>
          <div className="ml-3 inline-flex">
            <a
              href="https://nextjs.org/docs/app"
              target="_blank"
              rel="noreferrer"
            >
              <Button variant="outline" icon={<BookOpen className="size-6" />}>
                Next.js Docs
              </Button>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
