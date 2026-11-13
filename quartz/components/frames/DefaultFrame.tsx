import { PageFrame, PageFrameProps } from "./types"
import HeaderConstructor from "../Header"

const Header = HeaderConstructor()

/**
 * The default page frame — three-column layout with left sidebar, center
 * content (header + body + afterBody), and right sidebar, followed by a footer.
 *
 * This is the original Quartz layout, extracted from renderPage.tsx.
 */
export const DefaultFrame: PageFrame = {
  name: "default",
  render({
    componentData,
    header,
    beforeBody,
    pageBody: Content,
    afterBody,
    left,
    right,
    footer,
  }: PageFrameProps) {
    const russian =
      componentData.fileData.frontmatter?.lang === "ru" ||
      componentData.fileData.slug?.startsWith("ru/")
    return (
      <>
        <div class="left sidebar" id="pmg-navigation">
          {left.map((BodyComponent) => (
            <BodyComponent {...componentData} />
          ))}
        </div>
        <div class="center">
          <div class="page-header">
            {left.length > 0 && (
              <button
                type="button"
                class="pmg-navigation-toggle"
                aria-controls="pmg-navigation"
                aria-expanded="true"
                hidden
              >
                <span class="pmg-navigation-hide">
                  {russian ? "Скрыть навигацию" : "Hide navigation"}
                </span>
                <span class="pmg-navigation-show">
                  {russian ? "Показать навигацию" : "Show navigation"}
                </span>
              </button>
            )}
            <Header {...componentData}>
              {header.map((HeaderComponent) => (
                <HeaderComponent {...componentData} />
              ))}
            </Header>
            <div class="popover-hint">
              {beforeBody.map((BodyComponent) => (
                <BodyComponent {...componentData} />
              ))}
            </div>
          </div>
          <Content {...componentData} />
          <hr />
          <div class="page-footer">
            {afterBody.map((BodyComponent) => (
              <BodyComponent {...componentData} />
            ))}
          </div>
        </div>
        <div class="right sidebar">
          {right.map((BodyComponent) => (
            <BodyComponent {...componentData} />
          ))}
        </div>
        {footer.map((FooterComponent) => (
          <FooterComponent {...componentData} />
        ))}
      </>
    )
  },
}
